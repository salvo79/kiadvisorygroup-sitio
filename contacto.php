<?php
// Formulario «Cuéntenos su desafío»: recibe la solicitud del sitio (español o inglés) y la envía por correo a
// contact@kiadvisorygroup.com desde el propio dominio. «Responder» va directo al visitante. Responde JSON a sitio.js.
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

const DESTINO = 'contact@kiadvisorygroup.com';
const REMITENTE = 'contact@kiadvisorygroup.com'; // buzón del dominio: Hostinger exige un remitente propio
// Credenciales SMTP del buzón: archivo FUERA de public_html (no está en GitHub ni se puede leer desde la web).
// Contenido: <?php return ['usuario' => 'contact@kiadvisorygroup.com', 'clave' => '…'];
// Sin ese archivo se usa mail() de PHP, que Hostinger Mail puede descartar como remitente no autorizado.
const CONFIG_SMTP = __DIR__ . '/../config-correo.php';

function responder($codigo, $ok, $mensaje) {
    http_response_code($codigo);
    echo json_encode(['ok' => $ok, 'mensaje' => $mensaje], JSON_UNESCAPED_UNICODE);
    exit;
}
function campo($nombre, $max = 200) {
    $v = trim((string) ($_POST[$nombre] ?? ''));
    $v = str_replace(["\r", "\0"], '', $v);
    return mb_substr($v, 0, $max, 'UTF-8');
}

/** Envía por SMTP autenticado (smtp.hostinger.com:465, SSL). Devuelve true o el texto del error. */
function enviarSmtp(array $cfg, $para, $asunto, $cuerpo, array $cabeceras) {
    $host = $cfg['host'] ?? 'smtp.hostinger.com';
    $puerto = $cfg['puerto'] ?? 465;
    $esquema = $cfg['esquema'] ?? 'ssl'; // 'tcp' solo para pruebas locales
    $s = @stream_socket_client("$esquema://$host:$puerto", $errno, $errstr, 15);
    if (!$s) return "conexión SMTP: $errstr ($errno)";
    stream_set_timeout($s, 20);
    $leer = function () use ($s) {
        $r = '';
        while (($l = fgets($s, 515)) !== false) {
            $r .= $l;
            if (strlen($l) < 4 || $l[3] === ' ') break; // última línea de la respuesta
        }
        return $r;
    };
    $paso = function ($comando, $esperado) use ($s, $leer) {
        if ($comando !== null) fwrite($s, $comando . "\r\n");
        $r = $leer();
        if ((int) substr($r, 0, 3) !== $esperado) throw new Exception(trim($r) ?: 'sin respuesta');
    };
    try {
        $paso(null, 220);
        $paso('EHLO kiadvisorygroup.com', 250);
        $paso('AUTH LOGIN', 334);
        $paso(base64_encode($cfg['usuario']), 334);
        $paso(base64_encode($cfg['clave']), 235);
        $paso('MAIL FROM:<' . $cfg['usuario'] . '>', 250);
        $paso('RCPT TO:<' . $para . '>', 250);
        $paso('DATA', 354);
        $mensaje = implode("\r\n", array_merge(['Date: ' . date('r'), 'To: <' . $para . '>', 'Subject: ' . $asunto, 'Message-ID: <' . bin2hex(random_bytes(12)) . '@kiadvisorygroup.com>'], $cabeceras)) . "\r\n\r\n" . $cuerpo;
        $mensaje = preg_replace('/^\./m', '..', $mensaje); // puntos al inicio de línea (protocolo SMTP)
        $paso($mensaje . "\r\n.", 250);
        $paso('QUIT', 221);
    } catch (Exception $e) {
        fclose($s);
        return $e->getMessage();
    }
    fclose($s);
    return true;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') responder(405, false, 'Método no permitido');

$en = ($_POST['idioma'] ?? '') === 'en';
// Trampa para robots: un campo oculto que una persona deja vacío
if (campo('sitio_web') !== '') responder(200, true, 'ok');

$nombre = campo('nombre', 120);
$email = campo('email', 160);
$desafio = trim(str_replace("\0", '', (string) ($_POST['desafio'] ?? '')));
$desafio = mb_substr($desafio, 0, 5000, 'UTF-8');
$area = campo('area', 120);
if ($nombre === '' || $desafio === '' || $area === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    responder(422, false, $en ? 'Please complete your name, a valid email, the area of interest and your challenge.' : 'Complete su nombre, un correo válido, el área de interés y su desafío.');
}

// Límite sencillo por visitante: una solicitud cada 30 segundos
session_start();
if (isset($_SESSION['ultimo_envio']) && time() - $_SESSION['ultimo_envio'] < 30) {
    responder(429, false, $en ? 'Please wait a few seconds before sending again.' : 'Espere unos segundos antes de volver a enviar.');
}

$e = $en
    ? ['Name', 'Company', 'Job title', 'Email', 'Phone', 'Area of interest', 'Industry', 'Timeframe', 'Challenge', 'Initial consultation', 'Sent from kiadvisorygroup.com (English site)']
    : ['Nombre', 'Empresa', 'Cargo', 'Correo', 'Teléfono', 'Área de interés', 'Industria', 'Horizonte', 'Desafío', 'Consulta inicial', 'Enviado desde kiadvisorygroup.com (sitio en español)'];
$empresa = campo('empresa', 160);
$cuerpo = implode("\n", [
    $e[0] . ': ' . $nombre,
    $e[1] . ': ' . ($empresa ?: '—'),
    $e[2] . ': ' . (campo('cargo', 120) ?: '—'),
    $e[3] . ': ' . $email,
    $e[4] . ': ' . (campo('telefono', 40) ?: '—'),
    $e[5] . ': ' . $area,
    $e[6] . ': ' . (campo('industria', 120) ?: '—'),
    $e[7] . ': ' . (campo('horizonte', 60) ?: '—'),
    '',
    $e[8] . ':',
    $desafio,
    '',
    '— ' . $e[10] . ' · ' . date('Y-m-d H:i') . ' · IP ' . ($_SERVER['REMOTE_ADDR'] ?? ''),
]);

$asunto = '=?UTF-8?B?' . base64_encode($e[9] . ' · ' . ($empresa ?: $nombre)) . '?=';
$nombreRespuesta = '=?UTF-8?B?' . base64_encode($nombre) . '?=';
$cabeceras = [
    'From: KI Advisory & Strategy Group <' . REMITENTE . '>',
    'Reply-To: ' . $nombreRespuesta . ' <' . $email . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: base64',
];
$cuerpo = chunk_split(base64_encode($cuerpo), 76, "\r\n");

if (is_readable(CONFIG_SMTP)) {
    $cfg = include CONFIG_SMTP;
    $resultado = is_array($cfg) && !empty($cfg['usuario']) && !empty($cfg['clave']) ? enviarSmtp($cfg, DESTINO, $asunto, $cuerpo, $cabeceras) : 'config-correo.php incompleto';
} else {
    $resultado = mail(DESTINO, $asunto, $cuerpo, implode("\r\n", $cabeceras), '-f' . REMITENTE) ? true : 'mail() rechazó el envío';
}
if ($resultado !== true) {
    error_log('[contacto.php] ' . $resultado); // queda en el registro de errores de Hostinger, no se muestra al visitante
    responder(500, false, $en ? 'We could not send your request right now. Please try again in a few minutes.' : 'No pudimos enviar su solicitud en este momento. Intente de nuevo en unos minutos.');
}
$_SESSION['ultimo_envio'] = time();
responder(200, true, $en ? 'Thank you. Your request was sent; a partner will reply within one business day.' : 'Gracias. Su solicitud fue enviada; un socio le responderá en menos de 24 horas hábiles.');

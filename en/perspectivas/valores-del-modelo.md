# Model values · KI Advisory & Strategy Group

> The model doesn't just say what to do; it also says how much it is worth to change each thing. With a single example (a cream and a gel) we see the optimal value, activity, slack, shadow price, reduced cost, break-even, and elasticity.

Planning · how to read the results

# What the numbers reported by the model mean [← All insights](https://kiadvisorygroup.com/en/perspectivas/index.html)

InfinityWorkflow  [← Return to How the sales program decides](https://kiadvisorygroup.com/en/perspectivas/como-decide-el-plan-de-ventas.html)

Planning · how to read the results

# What the numbers reported by the model mean

The model doesn't just say **what to do**; it also says **how much it is worth to change** each thing. With a single example (a cream and a gel) we see the optimal value, activity, slack, shadow price, reduced cost, break-even, and elasticity.

Move the sliders: the numbers change just like in the model.

### Moisturizing cream

Price$100

Cost$40

Margin per unit$60

The market buys up to600 units

In inventory500 units

### Exfoliating gel

Price$40

Cost$45

Margin per unit−$5

The market buys up to200 units

In inventory300 units

## 1 · Optimal value and activity also: **objective function (Z)** · **primal solution** · **variable value**

What is the best that can be achieved, and by doing what?

The model tests all combinations and chooses the one with the highest margin: Cream: sells **500** units × $60 = **$30,000** Gel: sells **0** units (each unit loses $5) Z = $30,000

The **optimal value** is the best possible profit under the business rules. The **activity** is how much of each thing the plan makes: 500 units of cream and 0 of gel. No other combination yields more.

## 2 · Active constraint and slack also: **limit** · **constraint activity** · **slack**

Which rule is holding back the plan?

Cream inventory: uses **500** of **500** → slack **0** active: binding Cream demand: uses **500** of 600 → slack **100** not binding

A constraint is **active** (or binding) when it is fully used (slack 0): it is the one preventing us from earning more. The one with slack does not get in the way. Here, inventory rules, not the market.

## 3 · Shadow price also: **shadow price** · **dual value** · **marginal value of a constraint**

If I had one more unit of inventory, how much would I earn?

Cream inventory 500 units

Shadow price of inventory $60 per unit Each additional unit is sold and yields $60. It is worth buying until the market is saturated (600 units).

The **shadow price** (or **dual value**) is the slope of the profit: how much Z increases if a constraint is relaxed by one unit. Only active constraints have it. Note: **it is valid within a range**. Beyond 600 units, the market rules, and an additional unit of inventory is worth $0; now the shadow price belongs to demand.

## 4 · Reduced cost and break-even also: **reduced cost** (of a variable) · **equilibrium value** · **equilibrium price**

Why isn't gel being sold, and at what price would it be worth it?

Gel price $40

Reduced cost of selling gel −$5 per unit Break-even (equilibrium price): **$45** If we forced the sale of one unit, profit would drop by $5. That is why the model leaves it at zero.

The **reduced cost** of a variable that the plan leaves at zero tells us how much it would cost to force it. The **break-even** is the price (or cost) at which it starts to become profitable: here, $45. A variable that is already profitable (like the cream) has a reduced cost of 0 and no break-even.

## 5 · Price elasticity also: **elasticity of demand** · **price sensitivity**

If I raise the price of the cream, how much sales do I lose?

Cream elasticity −2.0

Price change +10 %

Demand elastic Units: **−17 %** · Revenue: **−9 %** · Margin: **−10 %** Price that maximizes margin: **$80**

The **elasticity** is how much the units sold change for every 1% increase in price (−2: raising the price by 1% lowers sales by 2%). If it is **elastic** (greater than 1 in absolute value), lowering the price increases revenue; if it is **inelastic**, raising the price increases it. The model measures it using the history of each product, and if you activate it, the demand of a scenario responds to its price.

On decisions (variables)

### How much of each thing to make?

- **Activity**: how much the plan makes (units to sell, buy, hold).

- **Min / Max**: the range within which it can move.

- **Reduced cost**: how much it would cost to force one more unit of something that is not profitable.

- **Break-even**: the price or cost at which it would start to be profitable.

On rules (constraints)

### What holds back the plan and how much is it worth to relax it?

- **Activity**: how much of the limit is used.

- **Slack**: how much is left over; 0 = active and binding.

- **Shadow price**: how much the plan would gain if the limit increased by one unit.

- **Range**: how far that value is valid before another rule takes over.

## In a table

ConceptoOther namesAnswersIn the exampleWhere it is seen

Optimal valueObjective function, ZWhat is the best possible outcome?$30,000Results › header

ActivityPrimal, variable valueHow much to do?500 units of cream, 0 of gelActivity report › Variables

SlackSlackHow much is left of the limit?Inventory 0 · demand 100Activity report › Constraints

Shadow priceShadow price, dual valueHow much is it worth to relax a rule?$60 per unit of inventoryConstraints · Inventories

Reduced costReduced costHow much does it cost to force something?−$5 per unit of gelActivity report › Variables

Break-evenEquilibrium value or priceAt what price does it become profitable?Gel at $45Variables · Products

ElasticityPrice sensitivityHow much do sales drop if the price increases?−2 → +10% price = −17% unitsProducts · Gantt · Excel

## The idea in one sentence

The **optimal value** tells us how much can be earned; the **activity**, what to do; the **shadow price**, which limit is worth expanding; the **reduced cost** and the **break-even**, what is not profitable and at what price it would be; and the **elasticity**, how the market reacts to price.  [← Return to How the sales program decides](https://kiadvisorygroup.com/en/perspectivas/como-decide-el-plan-de-ventas.html)

---

Source: https://kiadvisorygroup.com/en/perspectivas/valores-del-modelo.html · KI Advisory & Strategy Group · contact@kiadvisorygroup.com

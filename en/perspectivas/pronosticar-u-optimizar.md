# Forecast or optimize · KI Advisory & Strategy Group

> Time series look at the past to tell you how much will be sold. The LP model takes that and decides how much is best to sell and buy to earn more without breaking business rules. They do not compete: one predicts and the other decides.

Two ways to plan

# Forecast or optimize [← All insights](https://kiadvisorygroup.com/en/perspectivas/index.html)

InfinityWorkflow  [← Back to How the sales program is decided](https://kiadvisorygroup.com/en/perspectivas/como-decide-el-plan-de-ventas.html)

Two ways to plan

# Forecast or optimize

**Time series** look at the past to tell you **how much will be sold**. The **LP model** takes that and decides **how much is best to sell and buy** to earn more without breaking business rules. They do not compete: one predicts and the other decides.

The forecast is the weather report. LP is deciding what to do with that weather.

The weather tells you it will probably rain tomorrow. It doesn't tell you whether it's best to cancel the delivery, change the route, or bring more umbrellas to the store: that depends on your trucks, your costs, and your inventory. That second part is what the LP model solves.

Time series (forecast)

"How much are we going to sell?"

It looks for the **trend** and **seasonality** in what already happened and projects them forward (moving average, regression, ARIMA). It delivers a figure per month and how reliable it is: the band opens up because the further out, the less certainty.

it doesn't know how much is in the warehouse or how much margin each unit leaves   LP model (optimization)

"How much is it best for us to sell?"

It takes demand as a **ceiling** and combines everything at once: margin, inventory, purchases, delivery times, budget, and targets. It delivers **decisions**: what to sell, where, when, and how much to buy, and which rule limits profitability.

it needs to know how much the market is asking for: that's where the forecast comes in

The same month, planned both ways

## The forecast calls for 130 units, but there are only 100

Cream A: the forecast says 70 units and leaves $80 each. Serum B: the forecast says 60 and leaves $50. There are 100 units in the warehouse.

How the plan is builtCream ASerum BIs it feasible?Margin

Copy the forecast as is7060No: 30 units missing—

Cut the forecast proportionally5446Yes$6,620

LP model7030Yes$7,100

With the forecast alone, the plan is either impossible or leaves money on the table. LP uses the same forecast and chooses the distribution that yields the most.

Differences, point by point

## What each one does

Time seriesLP model

The questionHow much will be sold?How much is best to sell and buy?

What it looks atOnly the history of the variable (and its seasonality)Everything together: demand, margin, inventory, purchases, deliveries, budget, targets

What it deliversA figure per month with its confidence rangeDecisions by product, zone, and month, and the value of each constraint

Business rulesIt doesn't know themIt respects them all; a plan that breaks a rule does not exist

MoneyIt doesn't distinguish what leaves more marginIt prioritizes what leaves the most margin

If something changesIt is adjusted again with new dataThe data is changed (price, cost, warehouse) and it recalculates in seconds

Its weak pointIt assumes the future resembles the pastIt is only as good as the demand we give it

In Infinity WorkflowData analytics › Case design (trends, ARIMA, and ARMA)Planning › LP sales optimization

The best is to use both

## One feeds the other

**1 · Forecast**Time series estimate how much the market demands each month.

**2 · Optimize**LP uses that forecast as a ceiling and builds the highest-margin plan.

**3 · Execute**The plan is distributed into targets per salesperson and sold.

**4 · Measure**What was actually sold becomes history and improves the next forecast.   [← Back to How the sales program is decided](https://kiadvisorygroup.com/en/perspectivas/como-decide-el-plan-de-ventas.html)

---

Source: https://kiadvisorygroup.com/en/perspectivas/pronosticar-u-optimizar.html · KI Advisory & Strategy Group · contact@kiadvisorygroup.com

import pandas as pd
import numpy as np
import quantopian.experimental.optimize as opt

def initialize(context):
    set_benchmark(symbol('XIV'))
    context.continues = [
        [continuous_future('VX', roll = 'calendar', offset = 1),0],
        [continuous_future('VX', roll = 'calendar', offset = 2),
        continuous_future('VX', roll = 'calendar', offset = 3)]
    ]
    schedule_function(rebalance, date_rule=date_rules.week_start(), time_rule=time_rules.market_open(hours=1))


def rebalance(context, data):
    context.short1 = data.current(context.continues[0][0], 'contract')
    context.short2 = data.current(context.continues[1][0], 'contract')
    context.long1 = data.current(context.continues[1][1], 'contract')
    targets = {context.short1:-0.33,
              context.short2: -0.33,
              context.long1: 0.33}
    
    
    for x in range(len(targets)):
           order_optimal_portfolio(objective=opt.TargetPortfolioWeights(targets),
                           constraints=[])
    

# shortvix
Quantopian hedged short vix strategy proof of concept


This strategy is a proof of concept of a way to created a hedged replica of the XIV ETN. The strategy benefits from the high carry cost of VIX futures contracts, by shorting the second and thrid month contracts (33% of NAV each) and collecting the perpetual contango. To hedge against spikes in the VIX and backwardation, the algorithm is long 33% of NAV on the fourth month contract.

I chose to short the second and third months instead of the first and second months (which is what the XIV does) to reduce volatilty of the short contracts and concentrate exposure more on contango. To hedge against increases in the VIX, the algorithm buys the fourth month contracts so that the portfolio has less exposure to the price of the VIX as well as the hedged position suffering less from contango by buying a longer dated contract.

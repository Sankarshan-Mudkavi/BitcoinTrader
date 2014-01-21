Bitcoin Trader
----
A short script that texts you when it seems like a good idea to buy/sell bitcoins.

 - The plist works for OSX (Linux users will have to write their own cron files).

 - To *install* the script use *git clone* and put the plist file into your LaunchAgents directory (Usually found in */Library*) 

 - Install the necessary dependencies (The Twilio python API)

 - Replace the following paths with the ones that lead to your cloned directory:


    /Users/sankarshanmudkavi/bcheck/PriceGraph.png


 - Then the script will run every hour and let you know if the price goes from a rise to a drop.

It's still a bit hacky so please report any issues on the issues page. However, I will be updating it with more functionailty in the coming weeks.


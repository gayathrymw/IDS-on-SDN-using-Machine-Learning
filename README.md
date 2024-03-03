Project Execution:

Create a mininet topology.

ssh to the mininet virtual machine.

Run the collectStats.py file on the ryu controller. (Data from collectStat.py file is used for training the algorithm.)

Now, run IDS_RyuApp.py to check whether current traffic is clean or malacious using machine learning algorithm.

sudo hping3 -c 10000 -d 120 -S -w 64 -p 80 --flood 10.0.0.2
sudo mn --cutom custom_topo.py --topo mytopo --controller=remote

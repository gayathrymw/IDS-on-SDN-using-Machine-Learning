from mininet.topo import Topo
from mininet.node import OVSSwitch, RemoteController

class SimpleCustomTopo(Topo):
    def build(self):
        # Adding switches
        s1 = self.addSwitch('s1', cls=OVSSwitch)

        # Adding hosts
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='10.0.0.3')
        h4 = self.addHost('h4', ip='10.0.0.4')

        # Adding links between switch and hosts
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s1, h3)
        self.addLink(s1, h4)

# This is required for the custom topology to be recognized by Mininet
topos = {
    'mytopo': SimpleCustomTopo,
}



## Project Execution:

Project Execution:

1. Run collectstats.py on the controller.
2. Then create a mininet custom topology. </br>
```sudo mn --cutom custom_topo.py --topo mytopo --controller=remote ```
4. (While collecting normal traffic label the data 0.)
5. Run some simple commands. So that you will be able to generate the clean data.
6. Stop the controller.
7. Change the collectstats.py file. Label the data as 1.
8. Start the controller and run collectstats.py file.
9. Create topology.
10. Run hping flood command to capture malicious data. </br>
```sudo hping3 -c 10000 -d 120 -S -w 64 -p 80 --flood 10.0.0.2``` 
11. Now stop the controller.
12. Run ryuapplication.py on the controller.
13. Create a topology.
14. Test the model on the new traffic.




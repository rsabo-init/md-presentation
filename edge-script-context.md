Edge scripts 

InView is SCADA like platfrom. It's all variable based, means that each tag, each sensor reading is a variable.
Variable can have multiple soruces: it can be read directly from the source, or via gateway protocol or to be only 'internal'.
Internal variables are helping ones that allows user to calculate some buissnes logic.

One of the ways to calculate interal variables is to write iws scripts.
IWS scripts are c# like code with integrated variables management into it.
All iws scripts are executed in the cloud.
---
i3x is our smart gateway, that we pun on the hardware at the field to communicate to devices and get readings on basic protocols like modbus and s7.
on the other hand i3x sends data to the platform, all variable based.
---
edge scripts are new version ove scripts, similar to iws scripts, that can be downloaded to the i3x gateway. They are executed localy on the i3x gateway.
We call them edge, because they are executed on the edge of the network.
Edge scripts are custom written code with integarted variables management that is executed on i3x gateway.
It gives us a benefit to make these scripts executable and funcional even when location is not connected on the cloud.
They do have option to read data from cloud which give them ability to DCS (Disctributed computing system) behavior, as remote locations can comunicate toghether.
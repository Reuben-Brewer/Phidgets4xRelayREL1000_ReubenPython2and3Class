########################

Phidgets4xRelayREL1000_ReubenPython2and3Class

Wrapper (including ability to hook to Tkinter GUI) to control Phidgets four-relay controller REL1000 (VINT).

From Phidgets' website:
"The REL1000 is a mechanical relay that will let you control the power circuits of as many as four separate devices.
This Phidget connects to your computer through a VINT Hub.
Control up to four separate devices.
Rated for 210W of DC power or 1750 VA of AC power.
DC applications - switch a circuit of up to 30V at 7A.
AC applications - switch up to 12A or 277V AC, as long as the total power doesn't exceed 1750 VA.
Requires external Power supply.
Isolation - A voltage spike on the load side of the relay will not damage the control side."

4x Relay Phidget
ID: REL1000_0
https://phidgets.com/?tier=3&catid=46&pcid=39&prodid=966

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision E, 07/18/2022

Verified working on: 
Python 2.7, 3.8.
Windows 8.1, 10 64-bit
Raspberry Pi Buster 
(no Mac testing yet)

*NOTE THAT YOU MUST INSTALL BOTH THE Phidget22 LIBRARY AS WELL AS THE PYTHON MODULE.*

###########################

########################### Python module installation instructions, all OS's

Phidgets4xRelayREL1000_ReubenPython2and3Class, ListOfModuleDependencies: ['future.builtins', 'Phidget22']
Phidgets4xRelayREL1000_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['future.builtins', 'MyPrint_ReubenPython2and3Class']
Phidgets4xRelayREL1000_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins']
Phidgets4xRelayREL1000_ReubenPython2and3Class, ListOfModuleDependencies_All: ['future.builtins', 'MyPrint_ReubenPython2and3Class', 'Phidget22']

https://pypi.org/project/Phidget22/#files

To install the Python module using pip:
pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"

###########################

########################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

###########################

########################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

###########################

########################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -
sudo apt-get install -y libphidget22
 
###########################
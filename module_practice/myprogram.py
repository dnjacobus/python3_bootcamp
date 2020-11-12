#This acts as the main program to be run

from mymodule import my_func #this module is in the program directory, but not in a package

from MyMainPackage import some_main_script #from the main package 

from MyMainPackage.SubPackage import mysubscript #from the subpackage

my_func() #my_func() can be called directly because the module itself was imported

some_main_script.report_main() #need to have package.func() bc only the package was imported

mysubscript.sub_report()
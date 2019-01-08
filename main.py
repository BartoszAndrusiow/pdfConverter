import sys;
sys.path.append(r'/Forms')
from Forms.Apps import *;

root=Tk();

root.title("Main")

apps=Apps(root);

root.mainloop()
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math
import json
f = open("eurocodes.json", "r")
database = json.loads(f.read())
concretes = database["Eurocodes"]["Materials"]["Concrete"]["Classes"]

# %% [markdown]
# ## Dados geométricos

# %%
A = 0.2
I = 0.04
Zg  = 0.6
H = 1.0
ap = 0.15
Wi = I/Zg
Ws = I/(H-Zg)

# %% [markdown]
# ## Dados ações

# %%
Med = 1000
Ned = 0

# %% [markdown]
# ## Dados pré-esforço

# %%
conc_class_name = "C25/30"
conc = concretes[conc_class_name]
Po = 1000
ep = Zg-ap


# %%
Sig_inf = -Po/A+Ned/A-Po*ep/Wi+Med/Wi
Sig_sup = -Po/A+Ned/A+Po*ep/Ws-Med/Ws


# %%
print (Sig_inf)
print (Sig_sup)


# %%

fck = conc["fck"]
fctm = conc["fctm"]
print (fctm)


# %%




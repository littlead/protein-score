# Python Version 3.7.3

class Aminoacid:

    def __init__(self, name, polar, hydrophobic, small, charged, tiny, aliphatic, aromatic, ve_pos, ve_neg):
        self.name = name
        self.polar = polar
        self.hydrophobic = hydrophobic
        self.small = small
        self.charged = charged
        self.tiny = tiny
        self.aliphatic = aliphatic
        self.aromatic = aromatic
        self.ve_pos = ve_pos
        self.ve_neg = ve_neg


p = Aminoacid(name='P', polar=False, hydrophobic=False, small=True, charged=False, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
a = Aminoacid(name='A', polar=False, hydrophobic=True, small=True, charged=False, tiny=True, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
g = Aminoacid(name='G', polar=False, hydrophobic=True, small=True, charged=False, tiny=True, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
c = Aminoacid(name='C', polar=True, hydrophobic=True, small=True, charged=False, tiny=True, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
s = Aminoacid(name='S', polar=True, hydrophobic=False, small=True, charged=False, tiny=True, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
n = Aminoacid(name='N', polar=True, hydrophobic=False, small=True, charged=False, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
t = Aminoacid(name='T', polar=True, hydrophobic=True, small=True, charged=False, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
v = Aminoacid(name='V', polar=False, hydrophobic=True, small=True, charged=False, tiny=False, aliphatic=True, aromatic=False, ve_pos=False, ve_neg=False)
c = Aminoacid(name='C', polar=False, hydrophobic=True, small=True, charged=False, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
d = Aminoacid(name='D', polar=True, hydrophobic=False, small=True, charged=True, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=True)
e = Aminoacid(name='E', polar=True, hydrophobic=False, small=False, charged=True, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=True)
h = Aminoacid(name='H', polar=True, hydrophobic=True, small=False, charged=True, tiny=False, aliphatic=False, aromatic=True, ve_pos=True, ve_neg=False)
k = Aminoacid(name='K', polar=True, hydrophobic=True, small=False, charged=True, tiny=False, aliphatic=False, aromatic=False, ve_pos=True, ve_neg=False)
r = Aminoacid(name='R', polar=True, hydrophobic=False, small=False, charged=True, tiny=False, aliphatic=False, aromatic=False, ve_pos=True, ve_neg=False)
y = Aminoacid(name='Y', polar=True, hydrophobic=True, small=False, charged=False, tiny=False, aliphatic=False, aromatic=True, ve_pos=False, ve_neg=False)
w = Aminoacid(name='W', polar=True, hydrophobic=True, small=False, charged=False, tiny=False, aliphatic=False, aromatic=True, ve_pos=False, ve_neg=False)
q = Aminoacid(name='Q', polar=True, hydrophobic=False, small=False, charged=False, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
i = Aminoacid(name='I', polar=False, hydrophobic=True, small=False, charged=False, tiny=False, aliphatic=True, aromatic=False, ve_pos=False, ve_neg=False)
l = Aminoacid(name='L', polar=False, hydrophobic=True, small=False, charged=False, tiny=False, aliphatic=True, aromatic=False, ve_pos=False, ve_neg=False)
m = Aminoacid(name='M', polar=False, hydrophobic=True, small=False, charged=False, tiny=False, aliphatic=False, aromatic=False, ve_pos=False, ve_neg=False)
f = Aminoacid(name='F', polar=False, hydrophobic=True, small=False, charged=False, tiny=False, aliphatic=False, aromatic=True, ve_pos=False, ve_neg=False)



s1 = [g, w, w, p, d, t]
s2 = [w, r, r, k, h, y]


score = 0

for acid in range(0, len(s1)):
    if s1[acid].name == s2[acid].name:
        print("Amino acids {} and {} get a score of +5".format(s1[acid].name, s2[acid].name))
        score += 5
        print("Running total: {}".format(score))
    elif s1[acid].hydrophobic == True and s2[acid].hydrophobic == True:
        print("Amino acids {} and {} get a score of +1".format(s1[acid].name, s2[acid].name))
        score += 1
        print("Running total: {}".format(score))
    elif (s1[acid].hydrophobic == True and s2[acid].hydrophobic == False) or (s1[acid].hydrophobic == False and s2[acid].hydrophobic == True):
        print("Amino acids {} and {} get a score of -5".format(s1[acid].name, s2[acid].name))
        score -= 5
        print("Running total: {}".format(score))
    else:
        print("Amino acids {} and {} get a score of 0".format(s1[acid].name, s2[acid].name))
        score += 0
        print("Running total: {}".format(score))

print("The final score is {}".format(score))

import nbformat
import re


# Lecture du fichier ipynb
with open(f'DataSet/Joly_Pierre.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# on recupere toutes les cellules avec une note 
for i, cell in enumerate(nb['cells']):
    if "note00" in cell['source'] :
        note00=cell['source']

    elif "note01" in cell['source'] :
        note01=cell['source']

    elif "note1" in cell['source'] :
        note1=cell['source']

    elif "note2" in cell['source'] :
        note2=cell['source']

    elif "note3" in cell['source'] :
        note3=cell['source']
    
    elif "note4" in cell['source'] :
        note4=cell['source']
    
    elif "note5" in cell['source'] :
        note5=cell['source']
        break

note_liste_enchar=[note00,note01,note1,note2,note3,note4,note5]
note_liste_int=[]

for i in note_liste_enchar:
    a ='\n'.join(i.splitlines()[1:])

    a=re.findall('\d',a)
    note_liste_int.append(int(a[len(a)-1]))


ponderations = [2, 2, 3, 2, 4, 1]
totaux = [7, 12, 10, 17, 14, 12]
notes = [note_liste_int[0]+note_liste_int[1], note_liste_int[2], note_liste_int[3], note_liste_int[4], note_liste_int[5], note_liste_int[6]]

#print(notes, sum(notes), ponderations)
note_ponderee_somme = 0 

for note, ponderation, total in zip(notes, ponderations, totaux):
    #print("je vais multiplier la note : ", note, "par le coeff", ponderation)
    note_ponderee_somme+= ponderation*(note*20)/total

#print("note ponderee somme : ", note_ponderee_somme, "somme coeff : ", sum(ponderations))
note_ponderee20 = round(note_ponderee_somme/sum(ponderations),1)

print("Votre note est : ", note_ponderee20, "/20")
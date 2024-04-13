#writing in a file using writelines() function:

f1 = open("Friends.txt","a")
friends = ["Madhuri\n","Vaishnavi\n","Aditi\n","Bhakti\n"]
f1.writelines(friends)
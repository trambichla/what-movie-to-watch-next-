import spacy
nlp = spacy.load('en_core_web_md')
Planet_Hulk_des = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
model_film = nlp(Planet_Hulk_des)
similarity_list ={}

def returnmovie():
    with open ('movies.txt', 'r') as f:
        f1 = f.readlines()
        for i in f1:
            content = i.split(":")
            content1 = content[1]
            compare_des = nlp(content1).similarity(model_film)

            similarity_list.update({content[0]:compare_des})
            #print(similarity_list)
            #print(content[0] + " - ", str(compare_des))     
            
    f.close()  

    v = list(similarity_list.values())
    k = list(similarity_list.keys())
    matched_film = k[v.index(max(v))]
           
    print("The next movie you should watch is", matched_film)  

returnmovie()

#Let us build a system that will tell you what to watch next based on the word vector similarity of the description of movies.       
        

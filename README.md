# cool-stuf
somes usefull code project you can use to code quicker 

# eportfolio

// créer un repository sur github

// créer un repository locale dans un fichier avec git init ( faire en sorte qu'il n'existe pas déja un .git dans le repertoire)

// dans le repertoire faire : 

git add . (pour all)

git remote add origin "lien recuperer sur l'onglet code du repository sur github" en ssh

git branch -M main 
git commit -m "message"
  
git push -u origin main 

" si ça ne fonctionne pas faire " 

git pull origin main --allow-unrelated-histories

fermer le gitbash 

retrouner dans le repertoire puis entrer 

//////////////////////////////////////////////////////////


// pour créer une paire de clé ssh
> ssh-keygen -t ed25519 -C "mbguyexau@gmail.com" 
> touche entrer
> touche entrer
> touche entrer 

//  pour copier la clé public dans le presse papier
>  clip < ~/.ssh/id_ed25519.pub 

// ajout sur github

porfil > paramètre > ssh et gps keys  > new ssh key 

git push -u origin main 

// après avoir fait ça pour mettre à jour le repositoty il faut 

git add .
git commit -M "message à afficher"
git push origin main 

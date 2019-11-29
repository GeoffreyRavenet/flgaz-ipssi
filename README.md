# flgaz-ipssi

Découverte des outils - Rédigez un court texte répondant aux questions suivantes
    Que propose le site PythonAnywhere.com ?
    -spécialisé dans l'hébergement Python
    -La liste des modules Python supportés 
    -Plusieur environnement proposé:
        Python 2.6, 2.7, 3.3, 3.4
        iPython 2.6, 2.7, 3.3, 3.4 (Interactive Python Terminal... très en vogue)
        PyPy 2.7
        Bash Console
        MySql Console
     -Possible de créer un site pré-configuré pour Flask, DJango
     -Utilise les infrastructures d'Amazon EC2
     -Propose un compte "Beginner" (gratuit)
     -Propose des DB MySql

    Qu'est ce que FLASK ? Quels sites connus utilisent Flask ?
    -Flask est un framework python open source pour le developpement web.
    Son but principal est d'être léger, afin de garder la souplesse de la programmation Python, associé à un système de templates. 
    Il est distribué sous licence BSD
    
    - Un des sites connus est Lyft qui est l’application de covoiturage la plus dynamique aux États-Unis et est disponible dans plus de 200 villes,
    facilitant 14 millons de deplacements par mois.
    Il utilise les services utilisent NumPy, Pandas et PuLP pour répondre aux demandes via Flask, Gevent et Gunicorn.
    Il utilise SciPy pour lutter contre la fraude et Salt pour approvisionner des hôtes.
    
Description des actions réalisées
    Quelles étapes avez-vous suivi ?
    -creer depot git
    -git init / git remote add origin {url} / git commit / git push
    -creation de compte pythonanywhere
    -ouvrir la console pythonanywhere en bash
    -fair un git clone
    -aller dans file recuper le chemin de ton fichier
    -Puis rendez-vous sur web suivre les etepas pous ajouter une nouvelle web app, 
    ne pas oublier de selectionner flask pour notre cas
    
Confuguration du setting : 
LOGIN = "ton login"
MDP = "mot de passe de la base"
NAME_BDD = "nom de votre base de donnée"
HOST = "nom de votre host fournie par pythonanywhere"
    
    Quelles difficultés avez-vous rencontrées ?
    -Apprendre fonctionement pythonanywhere
    
Réflexions sur le projet
    Quels sont, selon vous, les aspects techniques limitants du projet FLGAZ dans l'état initial ?
    -le nombre de charge suporter est limiter
    -design inexistant
    -pas de date de publication
    -pas d'import de fichier(image, video)
    -pas le login/logout
    -impossible de modifier ses message
    -pas message personnaliser 
    -systeme de stockage
    -manque les likes
    -les retweetes
    
    Quelles sont, selon vous, les menaces auxquelles un tel projet peut être soumis ?
    - file d'injection
    - surcharge du serveur
    - droit de stockage
    - droit d'auteur
    - limation de stockage
    

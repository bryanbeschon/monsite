# monsite

Le code utilise les technologies suivantes :
- Django 1.8.19
- Python 2.7.10
- Bootstrap 3.3.7
- Jquery 3.1.1

Principe :
- Se connecter avec un des comptes existants (ou créer un utilisateur si besoin via le lien "S'inscrire ici")
- Une fois connecté, on arrive sur une page sur laquelle on voit ses informations. On dispose également d'un bouton "Mettre à jour les informations" qui permet d'accéder à une modale où l'on peut changer son adresse mail. La modification a alors lieu directement sur la page principale (sans rechargement) et dans la base de données.
- On peut se déconnecter du compte en allant dans le menu "Paramètres" à droite puis en cliquant sur "Se déconnecter". On revient alors sur la page de connexion.

Exemples d'utilisateurs existants :
- Utilisateur 1 :

  Nom d'utilisateur : user1

  Prénom : userprénom

  Nom : usernom

  Adresse mail : user1@gmail.com

  Mot de passe : user1

- Utilisateur 2 :

  Nom d'utilisateur : user2

  Prénom : user2prenom

  Nom : user2nom

  Adresse mail : user2@gmail.com

  Mot de passe : user2

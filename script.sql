/* ---------- Insertion des clients ---------- */
insert into mainapp_clients(name, email, phone, profession) 
values('Roger Dumont', 'roger.dumont@email.be', '065 12 34 56', 'Employé section finance');

insert into mainapp_clients(name, email, phone, profession) 
values('Caroline Staquet', 'caronline.staquet@email.be', '065 00 11 22', 'Employée section marketing');

insert into mainapp_clients(name, email, phone, profession) 
values('Benjamin Libert', 'benjamin.libert@email.be', '065 58 42 71', 'Chef section finance');

insert into mainapp_clients(name, email, phone, profession) 
values('Amandine Minom', 'amandine.minom@email.be', '065 78 56 12', 'Employée section informatique');

/* ---------- Insertion des techniciens test (MDP EN CLAIR) ---------- */
insert into mainapp_users(username, password) 
values('test', 'test');

insert into mainapp_users(username, password) 
values('test2', 'test2');

/* ---------- Insertion des status ---------- */
insert into mainapp_status(status)
values('Pas commencée');

insert into mainapp_status(status)
values('En cours');

insert into mainapp_status(status)
values('Terminée');

/* ---------- Insertion des tâches ---------- */
/* Pas commencée */
insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Ajout RAM', 'Ajouter 4Go de RAM sur le PC', 'Bâtiment des finances, local 12', ' ', '2021-11-15 14:21:07', '2021-11-25 12:00:00', 1, 1, 1);

insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Problème serveur finance', 'Le serveur des finances crash souvent', 'Bâtiment des finances, local 2', ' ', '2021-10-10 13:58:26', '2021-10-11 12:00:00', 3, 1, 1);

insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Problème serveur finance', 'Le serveur des finances crash souvent', 'Bâtiment des finances, local 2', ' ', '2021-10-10 13:58:26', '2021-10-11 12:00:00', 3, 1, 2);

/* En retard */
insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Tâche en retard', 'Exemple d\'une tâche en retard', 'n/a', ' ', '1989-08-24 12:00:00', '1989-08-24 13:00:00', 3, 1, 1);

/* Commencée */
insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Remplacement écran', 'Ancien écran CRT à changer et reprendre', 'Bâtiment informatique, salle de formation', ' ', '2021-11-11 08:30:12', '2021-11-11 12:00:00', 4, 2, 1);

/* En retard */
insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Tâche en retard', 'Exemple d\'une tâche en retard', 'n/a', ' ', '1989-08-24 12:00:00', '1989-08-24 13:00:00', 1, 2, 1);

/* Finie */
insert into mainapp_tasks(title, description, location, note, startDate, endDate, client_id, status_id, user_id)
values('Oubli de mot de passe', 'réinitialiser le mot de passe du client', 'À distance', ' ', '2021-07-12 09:11:28', '2021-07-12 09:30:00', 2, 3, 1);

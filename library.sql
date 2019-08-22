insert into libraryapp_library
(title, address)
values
('Bellview Library', '500 Main Street');

insert into libraryapp_library
(title, address)
values
('Franklin Library', '1004 Franklin Hwy');

insert into libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
values
('Lamb', '59359409490', 2004, 1, 'Roger Moore', 1);

insert into libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
values
('Taiko', '04275747474873', 1997, 1, 'Saichi Nakamoto', 1);

insert into libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
values
('The Golem and the Jinni', '8592475822', 2013, 1, 'Helene Wecker', 2);




select * from auth_user;


select * from libraryapp_library;
select * from libraryapp_book;
delete from libraryapp_book where id > 4;
select * from libraryapp_librarian;



select
    l.id,
    l.location_id,
    l.user_id,
    u.first_name,
    u.last_name,
    u.email
from libraryapp_librarian l
join auth_user u on l.user_id = u.id
;
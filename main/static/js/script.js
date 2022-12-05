let Name = document.getElementById('id_name');
let email = document.getElementById('id_email');
let pswd = document.getElementById('id_password');

Name.insertAdjacentHTML('afterend', '<img src="/static/img/person.svg">')
pswd.insertAdjacentHTML('afterend', '<img src="/static/img/lock.svg">')
if (email != null) {
    email.insertAdjacentHTML('afterend', '<img src="/static/img/mail.svg">')
}

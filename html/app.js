const entrarClick = document.getElementById('entrarbtn')

entrarClick.addEventListener('click', function(event){
    event.preventDefault()
    let senha = document.getElementById('senha').value;
    let login = document.getElementById('login').value;
    let errata = document.getElementById('acessFail'); 

    if (login == 'admin' && senha == 'sccp@1910'){
    window.location.href = 'html/home.html'}
    else{
        errata.style.display = 'flex';
    }

});
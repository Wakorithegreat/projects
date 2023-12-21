function renderInfo() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    const renderedInfo = document.getElementById('renderedInfo');
    renderedInfo.innerHTML = <p><strong>Name:</strong> ${name}</p><p><strong>Email:</strong> ${email}</p>;
}
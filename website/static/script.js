document.getElementById('copied-button').addEventListener('click', function () {
    const popup = document.getElementById('copied-message');
    popup.style.display = 'block';

    const copyText = document.getElementById('new-url');
    copyText.select();
    navigator.clipboard.writeText(copyText.value)
        .then(() => {
            popup.style.display = 'block';
            setTimeout(function () {
                popup.style.display = 'none';
            }, 3000);
        })
        .catch(err => {
            console.error('Failed to copy: ', err);
        });
});
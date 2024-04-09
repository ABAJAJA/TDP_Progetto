# How to use

Il sito implementa diverse funzionalità, per esempio tramite le **API** è possibile **creare** dei post sul blog nella pagine principale tramite una semplice richiesta.

Python:
```py
    from requests import post

    URL = "http://127.0.0.1:5000/api/v1/createblogpost"

    header = { "X-Api-Token": "token_here" }

    data = {
        "title": "Test test test",
        "subtitle": "testino testino testino"
    }

    response = post(URL, data=data, headers=header)
    print(response.text)
```

JavaScript:
```js
const URL = "http://127.0.0.1:5000/api/v1/createblogpost";
const header = { "X-Api-Token": "token_here" };
const data = {
    title: "Test test test",
    subtitle: "testino testino testino"
};

async function createBlogPost() {
    try {
        const response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...header
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error('Error:', error);
    }
}

createBlogPost();
```
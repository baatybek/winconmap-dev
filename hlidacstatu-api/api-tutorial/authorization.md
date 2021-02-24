Authorization is performed using the authentication token assigned to you. An authorization token must be sent in the header of each API request.
Authorization token: e17e445d0285471db98ce9ed8ef698c1 (this is not an token for OCR Minion. See below)
Example of use:
curl -X GET https://www.hlidacstatu.cz/Api/v2/smlouvy/204737 -H 'Authorization: Token e17e445d0285471db98ce9ed8ef698c1'


Authorization is performed using the authentication token assigned to you. An authorization token must be sent in the header of each API request.



GET: https://www.hlidacstatu.cz/Api/v2/ping/{text} -> returns 'pong' + your text

GET: https://www.hlidacstatu.cz/Api/getmyip-> returns your ip address

GET: https://www.hlidacstatu.cz/Api/v2/dumps


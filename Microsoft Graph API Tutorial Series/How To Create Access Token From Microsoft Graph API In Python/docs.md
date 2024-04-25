# hogyan lehet hozzáférni a Microsoft Graph API-hoz Pythonnal?

## két módszer van:
1. A CondifentialClientApplication osztályt fogja használni
2. a másik a PublicClientApplication osztály

### a kettő közötti különbség, hogy a CondifentialClientApplication osztályt jogosultsági kódot generál, átadja az engedélyezőnek, hogy generáljon hozzáférési tokent. A PublicClientApplication osztály pedig a user nevében az alkalmazáshoz való hozzáférésre lesz szzükség.

# 1. módszer
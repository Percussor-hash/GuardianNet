Purpose of this Project :
Facilitate communication between multiple client systems via a common server. 
Working:
The server receives the query from the client and gives the corresponding response back to the client based on the query.
The server will communicate based on already predefined tokens which are fed into the server side. The server will search for these tokens and give the corresponding answer. Else, it will not give a response.
Along with this chatbot feature, clients can communicate freely with each other as in a chatroom.
Transport layer:
The TCP transport layer is used to send messages securely from clients to server. 


Additional Features:
Censorship has been implemented. In short, words have been weighted.
Slang words will not be tolerated on this platform. The message will not be sent to the other connected clients. And the sending client will receive a warning.
If intolerable words are used, the sending client will be kicked out of the chatroom. The other clients will receive a notification of the offending client’s departure, but the reason will not be made public.
Chat History will not be stored by server providing privacy to clients.

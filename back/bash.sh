curl --request POST \
  --url https://sandbox-api.coinpay.cr/api/auth/integration/createToken/v1 \
  --header 'Content-Type: application/json' \
  --data '{
  "IdRequest": "20221014141200",
  "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoiIGJlcmVubXgyMDE0QGdtYWlsLmNvbSAgIGJlcmVubXggIiwiQ2hlY2tzdW0iOiIxM2RjMDZhMTMxY2M3ZWEyNmQyZDQyYmFhYmE3NmExNmEwYTc3NDRmMDk5MDk3YjVmYTE0YWY5MzQ2YWRkNzZjIiwiSWRVc2VyIjoiMzkyNzIiLCJFbWFpbCI6IiBiZXJlbm14MjAxNEBnbWFpbC5jb20iLCJuYmYiOjE2NjYyODE2MzAsImV4cCI6MTY2NjI4MTkzMCwiaWF0IjoxNjY2MjgxNjMwfQ.ON7qAujDPBBVUTNDAYQ7lsDWpe_QfBVjIXsyGJhfU64"
  "Checksum": "cc993584e2eadd3e7fb76e3ab8f7c08099bdb300bba03c5798080f371f9260fd"
}'

## Receiver script from Sigfox backend to ThingSpeak

see the counterpart project bcf-sigfox-wind-station

```
pip install -r requirements.txt
python main.py
```

If you would like to test POST request

```
curl -X POST http://localhost:5000 -d "{\"data\": \"01000200\"}" -H"Content-Type: application/json"
```

# DIST-SYSTEMS

## Project 1

Podaci: https://huggingface.co/datasets/codeparrot/codeparrot-clean/resolve/main/file-000000000040.json.gz. 

Docker slike dostupne javno na: https://hub.docker.com/repositories/lukablaskovic. 

Baza podataka nije pohranjena na GIT-u. 
 
Za pokretanje aplikacije, pokrenite M1 uslugu pomoću jednog od sljedećih API poziva:
- localhost:1001/start 
- localhost:1001/start2  (M1+)


### Vyper - smart contract dio
Dobiveno preko https://remix.ethereum.org/
Potrebno je:
- instalirati i pokrenuti Ganache
- instalirati vyper i web3 python pakete
- instalirati vyper ekstenziju na remix.ethereum.org,
- stvoriti novi file (github.vy) i u njega kopirati kod iz smart-contract.py
- compile-anje koda, natrag vraca ABI.json i adresu
Deployanje koda putem https://remix.ethereum.org/

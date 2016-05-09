#! /bin/bash

# Start docker when giving you shit

YELLOW='\033[1;33m'
NC='\033[0m' # No Color

printf "${YELLOW}==> making docker work${NC}"
echo ""
echo ""

printf "${YELLOW}==> rm default vm${NC}"
echo ""
docker-machine rm default

printf "${YELLOW}==> Creating Virtual box VM${NC}"
echo ""
docker-machine create --driver virtualbox default


printf "${YELLOW}==> Setting VM default as default..${NC}"
echo ""
docker-machine env default

printf "${YELLOW}==> Configuring shell${NC}"
echo ""

eval $(docker-machine env default)
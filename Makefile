test:
	echo "TESTING STUFF"
cpush:
	git add .
	git commit -m "Testing"
	git push origin dev1
cpull:
	git fetch origin dev1
	git pull origin dev1
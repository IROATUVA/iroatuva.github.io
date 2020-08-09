@echo off
title IRO Data website maker
set /p bofa="do you want to run the Bank Account Program (Y/N)?"
pause
IF /I "%bofa%"=="y" (
	echo Commencing Bank Account Program
	pause
	python BoFA.py
	pause
)
echo Commencing website maker
python website_designer.py
cd iroatuva.github.io
pause
echo pushing to github...
git add --all
git commit -a -m "Automated message"
git push
pause
echo You are all done! Wait a few minutes for the website to update!
pause
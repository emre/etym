hooks:
	ln -s ../../.githooks/pre-commit .git/hooks/pre-commit

styles:
	sass ./static/css/main.scss > ./static/css/main.css

run:
	gunicorn etym:app

update:
	@./contrib/update-db
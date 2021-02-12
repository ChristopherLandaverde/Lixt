HOST=127.0.0.1
TEST_PATH=./

install:
	\virtualenv env; \
	pip install -r requirements.txt;\


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	name '*~' -exec rm -f  {}
sql:
	cd migration; echo "I'm in migration directoy"; \
	cat *.sql  > all_files.sql;
	mysql -u root -p -e "source migration/all_files.sql";

test:
	. env/bin/activate; python rest.py
new:
	pyttest testapp.py
lint:
	pylint src/rest.py
	pylint src/testapp.py
	pylint src/db.py;

pytest:
	pytest src/testapp.py


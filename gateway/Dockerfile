FROM archlinux/base
run pacman -Syu --noconfirm \
	base-devel \
	python \
	python-pip \
	vim \
	git \
	python-flask \
	python-flask-sqlalchemy \
	python-flask-migrate \
	python-werkzeug \
	gunicorn
#COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
#RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
run pacman -U --noconfirm /app/builtPackages/*
ENTRYPOINT ["sh", "entrypoint.sh"]

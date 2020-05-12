FROM debian

ENV DB_USER dba
ENV DB_PASS password

RUN \
	# 设置时间
	rm /etc/localtime ;\
	ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime ;\

	# 修改apt源
	rm -f /etc/apt/sources.list ;\
	echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian buster main" >> /etc/apt/sources.list ;\
	echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main" >> /etc/apt/sources.list ;\
	echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian buster-updates main" >> /etc/apt/sources.list ;\

	# 安装mariadb，非必须软件不安装，最后清理
	apt update ;\
	apt install -y mariadb-server ;\
    apt clean
	
RUN \
	# 修改配置文件，允许外网访问
	sed -i -e 's/bind-address            = 127.0.0.1/#bind-address            = 127.0.0.1/g' /etc/mysql/mariadb.conf.d/50-server.cnf ;\

	# 编写容器启动脚本
	echo "#!/bin/bash" >> /opt/start.sh ;\
	echo "service mysql start" >> /opt/start.sh ;\
	# echo 'mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO \'\$DB_USER\'@\'%\' IDENTIFIED BY \'\$DB_PASS\' WITH GRANT OPTION;"' >> /opt/start.sh ;\
	# echo 'mysql -u root -e "flush privileges;"' >> /opt/start.sh ;\
	# echo "/bin/bash" >> /opt/start.sh ;\
	
	cat /opt/start.sh ;\
	# echo "mysqld_safe" >> /opt/start.sh ;\
	chmod u+x /opt/start.sh

#ENTRYPOINT ["/opt/start.sh"]
CMD ["/opt/start.sh"]
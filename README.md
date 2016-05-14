[![ZenHub] (https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png)] (https://zenhub.io)
# kujira-graphite
Service which is saving metrics from graphite-api to redis server. 
To be able to use library you have to copy config file to /etc :
* `cd kujira-api/kujira_graphite` 
* `cp config/kujira-graphite.cfg /etc/kujira-graphite.cfg`

It is also possible to start a caching service:
* change `ExecStart` in `service/kujira-graphite.service` to your `graphite_redis_script` location
* `cp service/kujira-graphite.service /etc/systemd/system/kujira-graphite.service`
* change config file `/etc/kujira-graphite.cfg` if necessary
* `systemctl daemon-reload` - to reload systemctl
* `systemctl enable kujira-graphite` - to start service during the system boot
* `systemctl start kujira-graphite` - to start service

Now you can check if kujira-graphite is active `systemctl status kujira-graphite` and check redis database.

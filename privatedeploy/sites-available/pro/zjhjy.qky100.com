server {
        listen 80;
        server_name     zjhjy.qky100.com *.zjhjy.qky100.com;
        error_log       /var/log/nginx/error.zjhjy.qky100.pro.log;
        access_log      /var/log/nginx/access.zjhjy.qky100.pro.log main;
        error_page 405 =200 $uri;
        
        location /      {
                proxy_pass http://99.99.99.99:9999;
                client_max_body_size     100m;
                client_body_buffer_size  128k;
                proxy_connect_timeout    1800;
                proxy_read_timeout       1800;
                proxy_send_timeout       18000;
                proxy_buffer_size        32k;
                proxy_buffers            4 64k;
                proxy_busy_buffers_size 128k;
                proxy_temp_file_write_size 512k;
                proxy_redirect  off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header   Cookie $http_cookie;	
                fastcgi_buffers      8 128K;
                }
}

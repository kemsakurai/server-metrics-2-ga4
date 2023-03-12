# server-metrics-2-ga4  
Google Analytics4でサーバーの統計情報を記録するためのツールです。    
サーバーに、当ツールを配置し、crontabでGoogle Analytics4のプロパティを指定して実行すると、指定したプロパティにサーバーのパフォーマンス統計情報がGoogle Analytics4のイベントとして記録されます。    

-------------------------------------------------------------
## 使用方法    

* git clone     
```console
git clone https://github.com/kemsakurai/server-metrics-4-ga.git    
```

* ライブラリインストール    
```console
pip install -r requirements.txt
```

* Script's argmrnts    
```console
Main Script's argments

optional arguments:
  -h, --help            show this help message and exit
  -mid MEASUREMENT_ID, --measurement_id MEASUREMENT_ID
                        Measurement Id of Google Analytics4.
  -a_secret API_SECRET, --api_secret API_SECRET
                        Api Secret of Google Analytics4.
  -cid CLIENT_ID, --client_id CLIENT_ID
                        Client Id of Google Analytics4.
```

* crontab example    
以下は、1分間隔で実行する例です。       
```console
*/1 * * * * /bin/python3.6 server_metrics_2_ga4.py -mid G-yyyyyyyy -a_secret xxxxxxxxxxxxxxxx -cid zzzzzzzzz &>> $LOG_DIR/server_metrics_2_ga4.log # server_metrics_2_ga4.log
```


------------------------------------------------------------
## Scripts    

* `server-metrics-2-ga4.py`    
取得するメトリクスをGAイベントとして送信するスクリプトです。       

------------------------------------------------------------

## Google Analytics のカスタム指標        

以下の指標をGoogle Analyticsに送信します。     
Google Analytics側にカスタム指標として作成する必要があります。      

|指標名|説明|スコープ|パラメーター名|測定単位|
|:---|:---|:---|:---|:---|
|非カーネル処理時間|ユーザー (非カーネル) のコードの実行に費やした時間|イベント|cpu_user|標準|
|ロードアベレージ5分間|過去5分間のロードアベレージ|イベント|loadavg5|標準|
|ロードアベレージ1分間|過去1分間のロードアベレージ|イベント|loadavg1|標準|
|ロードアベレージ15分間|過去15分間のロードアベレージ|イベント|loadavg15|標準|
|メモリー空き容量|メモリー空き容量|イベント|memory_available|標準|
|メモリー容量合計|メモリー容量合計|イベント|memory_total|標準|
|メモリー使用容量|メモリー使用容量|イベント|memory_used|標準|
|プロセッサーアイドル時間|プロセッサーアイドル時間 (プロセッサー・ティックで表される)|イベント|cpu_idle|標準|
|カーネル時間|カーネル・コードの実行に費やした時間 (プロセッサー・ティックで表される)|イベント|cpu_system|標準|
|swap空き領域|swap空き領域|イベント|swap_free|標準|
|swap容量合計|swap容量合計|イベント|swap_total|標準|
|swap利用領域|swap利用領域|イベント|swap_used|標準|
|network IO 送信時のエラー数|network IO 送信時のエラー数|イベント|net_io_errout|標準|
|network IO 送信パケット数|network IO 送信パケット数|イベント|net_io_packets_sent|標準|2023年3月11日|
|network IO 受信時のエラー数|network IO 受信時のエラー数|イベント|net_io_errin|標準|2023年3月11日|
|network IO 受信パケット数|network IO 受信パケット数|イベント|net_io_packets_recv|標準|2023年3月11日|
|disk領域合計|disk領域合計|イベント|disk_usage_total|標準|
|disk空き領域|disk空き領域|イベント|disk_usage_free|標準|
|disk利用領域|disk利用領域|イベント|disk_usage_used|標準|
|disk利用率|disk利用率|イベント|disk_usage_percent|標準|
|disk IO 読み込み回数|disk IO 読み込み回数|イベント|disk_io_read_count|標準|
|disk IO 読み込みバイト数|disk IO 読み込みバイト数|イベント|disk_io_read_bytes|標準|
|disk IO 書き込み回数|disk IO 書き込み回数|イベント|disk_io_write_count|標準|2023年3月13|
|disk IO 書き込みバイト数|disk IO 書き込みバイト数|イベント|disk_io_write_bytes|標準|
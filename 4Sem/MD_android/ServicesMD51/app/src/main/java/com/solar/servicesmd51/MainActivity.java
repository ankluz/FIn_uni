package com.solar.servicesmd51;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import android.app.Activity;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import java.net.BindException;

public class MainActivity extends Activity {
    private Intent ServiceIntent;
    private ServiceConnection conn;
    boolean bound = false;
    public NotificationManager notiMan;




    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ServiceIntent = new Intent(this, MyService.class);
        conn = new ServiceConnection() {
            @Override
            public void onServiceConnected(ComponentName componentName, IBinder iBinder) {
                bound = true;
            }

            @Override
            public void onServiceDisconnected(ComponentName componentName) {
                bound = false;
            }
        };
        NotificationChannel channel = new NotificationChannel(
                "CHANNEL_ID", "Regular notifications", NotificationManager.IMPORTANCE_DEFAULT);
        notiMan = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        notiMan.createNotificationChannel(channel);


        setContentView(R.layout.activity_main);
    }

    @RequiresApi(api = Build.VERSION_CODES.O)
    public void onstartClick(View view) {
        startForegroundService(ServiceIntent);
    }

    public void onbindClick(View view) {
        bindService(ServiceIntent, conn, BIND_AUTO_CREATE);
    }

    public void onUnbindClick(View view) {
        if (bound) {
            unbindService(conn);
        }
    }

    public void onStopClick(View view) {
        stopService(ServiceIntent);
    }

    public void notifi(View view){
        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(this, "CHANNEL_ID")
                        .setSmallIcon(R.drawable.ic_launcher_foreground)
                        .setContentTitle("Уведомляю")
                        .setContentText("Это прекрасно и оно работает")
                        .setPriority(NotificationCompat.PRIORITY_DEFAULT);


        Notification nf = builder.build();
        notiMan.notify(0, nf);


    }

}
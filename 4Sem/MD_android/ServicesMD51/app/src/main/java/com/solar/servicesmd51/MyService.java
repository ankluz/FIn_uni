package com.solar.servicesmd51;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Binder;
import android.os.Build;
import android.os.IBinder;
import android.util.Log;
import android.widget.Toast;

import androidx.annotation.RequiresApi;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;


public class MyService extends Service {

    private Notification createForegroundNotification() {
        NotificationManager notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);

        // Идентификатор уникального канала уведомлений.
        String notificationChannelId = "Foreground_notification";

        // Для систем выше Android8.0 создайте новый канал сообщений
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            // Видимое пользователем имя канала
            String channelName = "Foreground Service Notification";
            // Важность канала
            int importance = NotificationManager.IMPORTANCE_HIGH;
            NotificationChannel notificationChannel = new NotificationChannel(notificationChannelId, channelName, importance);
            notificationChannel.setDescription("Отображение постоянного уведомления нашего любимого приложения");
            if (notificationManager != null) {
                notificationManager.createNotificationChannel(notificationChannel);
            }
        }

        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, notificationChannelId);
        // Значок уведомления
        builder.setSmallIcon(R.drawable.ic_launcher_foreground);
        // Название уведомления
        builder.setContentTitle("Улыбнись");
        // Содержание уведомления
        builder.setContentText("Служба переднего плана отлично работает");
        // Устанавливаем время отображения уведомлений
        builder.setWhen(System.currentTimeMillis());
        // Устанавливаем содержимое автозагрузки
        Intent activityIntent = new Intent(this, MainActivity.class);
        Intent helloIntent = new Intent(this, MainActivity2.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 1, activityIntent, PendingIntent.FLAG_UPDATE_CURRENT);
        PendingIntent anotherIntent = PendingIntent.getActivity(this, 1, helloIntent, PendingIntent.FLAG_UPDATE_CURRENT);
        builder.addAction(R.drawable.ic_launcher_foreground, "StartMain",pendingIntent);
        builder.addAction(R.drawable.ic_launcher_background,"StartHello",anotherIntent);

        // Создаем уведомление и возвращаем
        return builder.build();
    }

    @Override
    public void onCreate(){
        super.onCreate();
        Toast.makeText(this,"Created", Toast.LENGTH_SHORT).show();
        Log.d("ServiceLifeCycle", "OnCreate called");
        Notification notification = createForegroundNotification();
        startForeground(1, notification);
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startID){
        Log.d("ServiceLifeCycle", "onStartCommand called");
        Toast.makeText(this,"Started", Toast.LENGTH_SHORT).show();
        return super.onStartCommand(intent,flags,startID);
    }

    @Override
    public void onDestroy(){
        super.onDestroy();
        Toast.makeText(this,"Destroyed", Toast.LENGTH_SHORT).show();
        Log.d("ServiceLifeCycle", "onDestroy called");
        stopForeground(true);
    }

    @Override
    public IBinder onBind(Intent intent) {
        Log.d("ServiceLifeCycle", "onBind called");
        Toast.makeText(this,"Bonded", Toast.LENGTH_SHORT).show();
        return new Binder();
    }

    @Override
    public boolean onUnbind(Intent intent){
        Log.d("ServiceLifeCycle","onUnbind called");
        Toast.makeText(this,"unBonded", Toast.LENGTH_SHORT).show();
        return super.onUnbind(intent);
    }
}
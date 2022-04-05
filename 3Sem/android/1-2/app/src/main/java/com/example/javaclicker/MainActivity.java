package com.example.javaclicker;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.google.android.material.snackbar.Snackbar;

public class MainActivity extends AppCompatActivity {

    private int mValue;
    private int holder;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView value = findViewById(R.id.value);
        TextView tooMany = findViewById(R.id.HowMany);

        findViewById(R.id.plus).setOnClickListener(v -> {
            mValue++;
            holder++;
            value.setText(String.valueOf(mValue));
            if(holder==0){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == 12){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == 13){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == 14){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%10 == 2){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%10 == 3){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%10 == 4){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else tooMany.setText("Всего "+ holder +" раз");

        });
        
        findViewById(R.id.minus).setOnClickListener(v -> {
            mValue--;
            holder++;
            value.setText(String.valueOf(mValue));
            if(holder==0){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == 12){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == 13){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == 14){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%10 == 2){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%10 == 3){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%10 == 4){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%100 == -12){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == -13){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%100 == -14){
                tooMany.setText("Всего "+ holder +" раз");
            }
            else if(holder%10 == -2){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%10 == -3){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else if(holder%10 == -4){
                tooMany.setText("Всего "+ holder +" раза");
            }
            else tooMany.setText("Всего "+ holder +" раз");

        });
        findViewById(R.id.reset).setOnClickListener(v -> {
            int oldValue = mValue;
            int oldHolder= holder;
            mValue = 0;
            holder = 0;
            value.setText(String.valueOf(mValue));
            tooMany.setText("Всего "+ holder +" раз");
            Snackbar.make(v, "Counter was reset", Snackbar.LENGTH_SHORT)
                    .setAction("Отмена", ignored -> {
                        mValue = oldValue;
                        holder = oldHolder;
                        value.setText(String.valueOf(mValue));
                        tooMany.setText("Всего "+ holder +" раз(a)");
                    })

                    .show();
        });

    }
}
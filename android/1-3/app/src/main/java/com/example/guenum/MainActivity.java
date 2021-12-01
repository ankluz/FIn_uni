package com.example.guenum;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    int rInt;
    int vvodInt;
    int randomer = 100;
    private Object Menu;
    TextView eT;




    public boolean onCreateOptionsMenu(android.view.Menu menu) {
        // TODO Auto-generated method stub
        getMenuInflater().inflate(R.menu.mymenu, menu);
        return super.onCreateOptionsMenu(menu);

    }

    public void onMenuClick(MenuItem item){
        Random random = new Random();
        rInt = random.nextInt(randomer);
        rInt++;
        TextView otvet = findViewById(R.id.t);
        otvet.setText("Игра начата заново, угадайте число");

    }
    public void onExitMenu(MenuItem item){
        this.finish();
    }

    public void onFirstLevelMenuClick(MenuItem item){
        TextView lbl = findViewById(R.id.infoLbl);
        randomer = 10;
        lbl.setText("Попробуйте угадать число (1 - "+randomer+")");
        Random random = new Random();
        rInt = random.nextInt(randomer);
        rInt++;
        TextView otvet = findViewById(R.id.t);
        otvet.setText("Игра начата заново, угадайте число");
    }

    public void onSecondLevelMenuClick(MenuItem item){
        TextView lbl = findViewById(R.id.infoLbl);
        randomer = 100;
        lbl.setText("Попробуйте угадать число (1 - "+randomer+")");
        Random random = new Random();
        rInt = random.nextInt(randomer);
        rInt++;
        TextView otvet = findViewById(R.id.t);
        otvet.setText("Игра начата заново, угадайте число");
    }

    public void onThirdLevelMenuClick(MenuItem item){
        TextView lbl = findViewById(R.id.infoLbl);
        randomer = 1000;
        lbl.setText("Попробуйте угадать число (1 - "+randomer+")");
        Random random = new Random();
        rInt = random.nextInt(randomer);
        rInt++;
        TextView otvet = findViewById(R.id.t);
        otvet.setText("Игра начата заново, угадайте число");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        EditText vvod = findViewById(R.id.eT);
        Button save = findViewById(R.id.b);
        TextView otvet = findViewById(R.id.t);

        Random random = new Random();
        rInt = random.nextInt(randomer);
        rInt++;


        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                vvodInt=Integer.parseInt(vvod.getText().toString());
                if(vvodInt>randomer){
                    otvet.setText("Ваше число вышло за диапазон");
                }
                else if(vvodInt<0){
                    otvet.setText("Ваше число вышло за диапазон");
                }
                else if(vvodInt==0){
                    otvet.setText("Сначала введите число");
                }
                else if(rInt>vvodInt){
                    otvet.setText("Число " + vvodInt+" меньше чем загаданное.");
                }
                else if(rInt<vvodInt){
                    otvet.setText("Число "+ vvodInt+" больше чем загаданное.");
                }
                else if(rInt==vvodInt){
                    otvet.setText(vvodInt+" является верно угаданным числом");
                }


            }
        });

        findViewById(R.id.exit).setOnClickListener(v -> {
            this.finish();
        });



    }

}
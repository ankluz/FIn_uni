package com.example.mainelements;

import androidx.appcompat.app.AppCompatActivity;


import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.os.Bundle;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Collections;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemClickListener {

    ListView mainListView;
    ArrayAdapter mArrayAdapter;
    ArrayList mNameList = new ArrayList();
    TextView mainTextView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mainTextView = findViewById(R.id.main_textview);
        mainTextView.setText("Set in Java!");


        EditText mainEditText;
        mainEditText = (EditText) findViewById(R.id.main_edittext);


        mainListView = findViewById(R.id.main_listview);

        mainListView.setAdapter(mArrayAdapter);
        mainListView.setOnItemClickListener(this);
        mArrayAdapter = new ArrayAdapter(this,
                android.R.layout.simple_list_item_1,
                mNameList);


        findViewById(R.id.main_button).setOnClickListener(g -> {
            mainTextView.setText(mainEditText.getText().toString() + " is learning Android development!");
            if (!mNameList.contains(mainEditText.getText().toString())) then:
                mNameList.add(mainEditText.getText().toString());
                Collections.sort(mNameList);
                mainListView.setAdapter(mArrayAdapter);
                mArrayAdapter.notifyDataSetChanged();
        });
        findViewById(R.id.ok_btn).setOnClickListener(v -> {
            mainTextView.setText("ОК");
            Toast.makeText(getApplicationContext(), "ОК", Toast.LENGTH_LONG).show();
        });
        findViewById(R.id.cnc_btn).setOnClickListener(v -> {
            mainTextView.setText("CANCEL");
            Toast.makeText(getApplicationContext(), "CANCEL", Toast.LENGTH_LONG).show();
        });


    }
    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Log.d("omg android", position + ": " + mNameList.get(position));
        mainTextView.setText(mNameList.get(position).toString()
                + " is learning Android development!");
    }

    @Override
    public void onClick(View view) {

    }
}

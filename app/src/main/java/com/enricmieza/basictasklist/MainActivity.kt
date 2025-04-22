package com.enricmieza.basictasklist

import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    private lateinit var taskEditText: EditText
    private lateinit var addButton: Button
    private lateinit var taskListView: ListView
    private val taskList = mutableListOf<String>()
    private lateinit var adapter: ArrayAdapter<String>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Inicialitzar vistes
        taskEditText = findViewById(R.id.taskEditText)
        addButton = findViewById(R.id.addButton)
        taskListView = findViewById(R.id.taskListView)

        // Configurar l'adaptador
        adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, taskList)
        taskListView.adapter = adapter

        // Afegir tasca
        addButton.setOnClickListener {
            val taskStr = taskEditText.text.toString()
            if (taskStr.isNotBlank()) {
                save(taskStr)
            }
        }

        // Eliminar tasca amb clic llarg
        taskListView.setOnItemLongClickListener { _, _, position, _ ->
            taskList.removeAt(position)
            adapter.notifyDataSetChanged()
            true
        }
    }

    private fun save(taskStr: String) {
        taskList.add(taskStr)
        adapter.notifyDataSetChanged()
        taskEditText.text.clear()
    }
}

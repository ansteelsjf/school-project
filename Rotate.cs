using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    // Start is called before the first frame update
    private float OffsetX = 0;
    private float OffsetY = 0;
    public float speed = 3f;
    void Start()
    {
      
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButton(0))
        {
            OffsetX = Input.GetAxis("Mouse X");
            OffsetY = Input.GetAxis("Mouse Y");

            transform.Rotate(new Vector3(OffsetY, -OffsetX, 0) * speed, Space.World);
        }
    }
}

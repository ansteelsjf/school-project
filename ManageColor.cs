using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ManageColor : MonoBehaviour
{
    // Start is called before the first frame update
    Color tempcolor;
    public Slider alphaSlider;
    void Start()
    {
        alphaSlider.value = 1f;
    }

    // Update is called once per frame
    void Update()
    {

        foreach (Transform trans1 in GetComponentInChildren<Transform>())
        {
            Material mat1 = trans1.gameObject.GetComponent<Renderer>().material;
            tempcolor = mat1.color;
            tempcolor.a = alphaSlider.value;
            mat1.color = tempcolor;
            

        }
        


    }
}

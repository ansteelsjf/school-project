using UnityEngine;
using System.Collections.Generic;
using System.Collections;
using System;
using System.IO;
using UnityEngine.UI;


namespace MarchingCubesProject
{
    public class Main : MonoBehaviour
    {
        public Material m_material;
        //public Material transparent_material;
        public int seed = 0;
        List<GameObject> meshes = new List<GameObject>();
        public GameObject currentGameObject;
        public float alpha = 0.2f;
        public Slider sliceslider;
        public RawImage rawimage;

        void Start()
        {

            int width = 274;
            int height = 384;
            int depth = 384;

            float[] voxels = new float[width * height * depth];
            float[,,] imageArray = new float[width, height, depth];
            float[,,] imageSlice = new float[height, depth, width];

            BinaryReader br;

            br = new BinaryReader(new FileStream("Assets/brain.nii", FileMode.Open));

            // the head of nii file is 348B, ignore head info
            br.ReadBytes(348);

            for (int w = 0; w < width; ++w)
            {
                for (int h = 0; h < height; ++h)
                {
                    for (int d = 0; d < depth; ++d)
                    {
                        float readData = br.ReadSingle();

                        imageArray[w, h, d] = readData;
                    }
                }
            }

            br.Close();
            //Segmentation
            for (int i = 0; i < width; ++i)
            {
                for (int j = 0; j < height; ++j)
                {
                    for (int k = 0; k < depth; ++k)
                    {
                        if (imageArray[i, j, k] > 40 || imageArray[i, j, k] < 10)
                        {
                            imageArray[i, j, k] = 0;
                        }


                    }
                }
            }

            sliceslider.value = 100;
            float someFloat = sliceslider.value;
            int someInt = (int)Math.Round(someFloat);

            Texture2D texture2D = new Texture2D(width, height);


            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    var val = imageArray[i, j, someInt];

                    if (val == 0)
                    {
                        texture2D.SetPixel(i, j, new Color(0, 0, 0));
                    }
                    else if (val == 1)
                    {
                        texture2D.SetPixel(i, j, new Color(1.0f, 1.0f, 1.0f));
                    }
                    else if (val == 255)
                    {
                        texture2D.SetPixel(i, j, new Color(1.0f, 0, 0));
                    }
                }
            }
            texture2D.Apply();
            rawimage.texture = texture2D;

            convert2Voxel(voxels, imageArray, width, height, depth);

            currentGameObject = gameObject;

            MarchingCubes marching = new MarchingCubes();
            marching.Surface = 0.5f;

            List<Vector3> gridpoints = new List<Vector3>();
            List<int> index = new List<int>();
            marching.Generate(voxels, width, height, depth, gridpoints, index);

            int maxVertsPerMesh = 30000;
            int numMeshes = gridpoints.Count / maxVertsPerMesh + 1;

            for (int i = 0; i < numMeshes; i++)
            {

                List<Vector3> splitVerts = new List<Vector3>();
                List<int> splitIndices = new List<int>();

                for (int j = 0; j < maxVertsPerMesh; j++)
                {
                    int idx = i * maxVertsPerMesh + j;


                    if (idx < gridpoints.Count)
                    {
                        splitVerts.Add(gridpoints[idx]);
                        splitIndices.Add(j);
                    }
                }


                if (splitVerts.Count == 0) continue;


                createmesh(splitVerts, splitIndices);

            }

        }

        void Update()
        {
            //transform.Rotate(Vector3.up, 10.0f * Time.deltaTime);

        }


        private int getIntLength(uint uLength)
        {

            return Convert.ToInt32(uLength);
        }

        private void convert2Voxel(float[] voxels, float[,,] imageArray, int width, int height, int depth)
        {
            for (int w = 0; w < width; w++)
            {
                for (int h = 0; h < height; h++)
                {
                    for (int d = 0; d < depth; d++)
                    {
                        voxels[w * height * depth + h * depth + d] = imageArray[w, h, d];
                    }
                }

            }

        }
        private void createmesh(List<Vector3> Verts, List<int> Indices)
        {
            List<Vector3> splitVerts = Verts;
            List<int> splitIndices = Indices;
            Mesh mesh = new Mesh();
            mesh.SetVertices(splitVerts);
            mesh.SetTriangles(splitIndices, 0);
            mesh.RecalculateBounds();
            mesh.RecalculateNormals();

            GameObject obj = new GameObject("Mesh");
            obj.transform.parent = transform;
            obj.AddComponent<MeshFilter>();
            obj.AddComponent<MeshRenderer>();
            Color oldColor = m_material.color;
            Color newColor = new Color(oldColor.r, oldColor.g, oldColor.b, alpha);
            Material transparent_material;
            transparent_material = m_material;
            transparent_material.SetColor("_Color", newColor);

            obj.GetComponent<Renderer>().material = transparent_material;
            obj.GetComponent<MeshFilter>().mesh = mesh;
            obj.transform.localPosition = new Vector3(-274 / 2, -384 / 2, -384 / 2);

            meshes.Add(obj);
        }
    }
}

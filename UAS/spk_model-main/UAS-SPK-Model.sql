PGDMP     	    $                {            UAS    15.4    15.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24587    UAS    DATABASE        CREATE DATABASE "UAS" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Indonesian_Indonesia.1252';
    DROP DATABASE "UAS";
                postgres    false            �            1259    24608    smartphonesamsung    TABLE       CREATE TABLE public.smartphonesamsung (
    id integer NOT NULL,
    brand character varying(65),
    ram character varying(20),
    processor character varying(65),
    rom character varying(65),
    baterai character varying(30),
    harga character varying(20)
);
 %   DROP TABLE public.smartphonesamsung;
       public         heap    postgres    false            �            1259    24607    smartphonesamsung_id_seq    SEQUENCE     �   CREATE SEQUENCE public.smartphonesamsung_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.smartphonesamsung_id_seq;
       public          postgres    false    220                       0    0    smartphonesamsung_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.smartphonesamsung_id_seq OWNED BY public.smartphonesamsung.id;
          public          postgres    false    219            o           2604    24611    smartphonesamsung id    DEFAULT     |   ALTER TABLE ONLY public.smartphonesamsung ALTER COLUMN id SET DEFAULT nextval('public.smartphonesamsung_id_seq'::regclass);
 C   ALTER TABLE public.smartphonesamsung ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220                      0    24608    smartphonesamsung 
   TABLE DATA           [   COPY public.smartphonesamsung (id, brand, ram, processor, rom, baterai, harga) FROM stdin;
    public          postgres    false    220   �       	           0    0    smartphonesamsung_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.smartphonesamsung_id_seq', 10, true);
          public          postgres    false    219            q           2606    24613 (   smartphonesamsung smartphonesamsung_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.smartphonesamsung
    ADD CONSTRAINT smartphonesamsung_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.smartphonesamsung DROP CONSTRAINT smartphonesamsung_pkey;
       public            postgres    false    220               �   x�}ҽn�0��~�;�R]_���V�����R�D���y��v���z�����l��3�!�C<M�"��5{����LP>Ј��I̋SuW*С\��]���¦~YIJ����J�W��4�a!^ q��QT���(��$!�3��>�ڦ����C��|��t�L��b�?ɨH����4��痹aL���aQcX�0�8͖$���{l�niN_4׮���	�8y���_��_8�_�䴫     